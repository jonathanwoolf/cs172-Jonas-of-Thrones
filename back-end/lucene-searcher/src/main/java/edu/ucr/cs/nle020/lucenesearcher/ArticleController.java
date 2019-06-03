// Andrew Pirelli, Matthew Lebouvier, Jonathan Woolf

package edu.ucr.cs.nle020.lucenesearcher;

import org.springframework.web.bind.annotation.*;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.queryparser.classic.MultiFieldQueryParser;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

import java.io.IOException;
import java.io.FileReader;
import java.io.File;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.nio.file.Paths;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

/**
 * Lucene simple demo. Based on:
 * https://lucene.apache.org/core/7_3_0/core/overview-summary.html#overview.description
 */

@RestController
@RequestMapping("/api")
@CrossOrigin("*")
public class ArticleController {
	int builtIndex = 0;
    static List<Article> articles;
    static {
        articles = new ArrayList<>();
        articles.add(new Article(1, "First Article",
                "Class Overview, Overview of Information Retrieval and Search Engines"));
        articles.add(new Article(2, "Second Article",
                "Ranking: Vector space model, Probabilistic Model, Language model"));
        articles.add(new Article(3, "Third Article",
                "Web Search: Spam, topic-specific pagerank"));
    }

    @GetMapping("/articles")
    public List<Article> searchArticles (
            @RequestParam(required=false, defaultValue="") String query) {
        if (query.isEmpty())
            return articles;
        if(builtIndex == 0) {
	        try {
	        	Analyzer analyzer = new StandardAnalyzer();

	            // Store the index in memory:
	            //Directory directory = new RAMDirectory();
	            // To store an index on disk, use this instead:
	            Directory directory = FSDirectory.open(Paths.get("index/data"));
	            IndexWriterConfig config = new IndexWriterConfig(analyzer);
	            IndexWriter indexWriter = new IndexWriter(directory, config);
	            JSONParser jsonParser = new JSONParser();
	            System.out.println("Before Tweet List");
	            File file = new File("tweets_1.json");
	            String path = file.getAbsolutePath();
	            System.out.println(path);
	            JSONArray tweetList = (JSONArray) jsonParser.parse(new FileReader("c:\\Users\\Andy\\Desktop\\search-webapp\\lucene-searcher\\test.json"));
	            System.out.println("Declared Tweet List");
	            for (Object o : tweetList) {
	                Document doc = new Document();
	                JSONObject tweetObject = (JSONObject) o;
	                doc.add(new TextField("title", (String) tweetObject.get("Author"), Field.Store.YES));
	                doc.add(new TextField("content", (String) tweetObject.get("Text"), Field.Store.YES));
	                indexWriter.addDocument(doc);
	            }
	            System.out.println("Iterated Tweet List");
	            indexWriter.close();
	            builtIndex = 1;
	        }
	        catch(IOException e) {
	        	List<Article> matches;
	            matches = new ArrayList<>();
	            matches.add(new Article(1, "IOException", "IOException"));
	            return matches;
	        } 
	        catch (org.json.simple.parser.ParseException e) {
	        	List<Article> matches;
	            matches = new ArrayList<>();
	            matches.add(new Article(1, "Parse Exception", "Parse Exception"));
	            return matches;
			}
        }
        // Now search the index:
        try {
	        try {
	        	Analyzer analyzer = new StandardAnalyzer();
	        	Directory directory = FSDirectory.open(Paths.get("index/data"));
	        	DirectoryReader indexReader = DirectoryReader.open(directory);
	        	IndexSearcher indexSearcher = new IndexSearcher(indexReader);
	
		        String[] fields = {"title", "content"};
		        Map<String, Float> boosts = new HashMap<>();
		        boosts.put(fields[0], 1.0f);
		        boosts.put(fields[1], 0.5f);
		        MultiFieldQueryParser parser = new MultiFieldQueryParser(fields, analyzer, boosts);
		        Query query1 = parser.parse(query);
		        System.out.println(query.toString());
		        int topHitCount = 100;
		        ScoreDoc[] hits = indexSearcher.search(query1, topHitCount).scoreDocs;
		        List<Article> matches;
		        matches = new ArrayList<>();
		        // Iterate through the results:
		        for (int rank = 0; rank < hits.length; ++rank) {
		            Document hitDoc = indexSearcher.doc(hits[rank].doc);
		            matches.add(new Article((rank + 1), "Score: " + Float.toString(hits[rank].score), hitDoc.get("content")));
		            // System.out.println(indexSearcher.explain(query, hits[rank].doc));
		        }
		        indexReader.close();
		        directory.close();
		        //matches.add(new Article(1, "Results Found", "Results Found"));
		        return matches;
	        }
	        catch(IOException e) {
	        	
	        }
        }
        catch(ParseException p) {
        	
        }
        List<Article> matches;
        matches = new ArrayList<>();
        matches.add(new Article(1, "No Results Found", "No Results Found"));
        return matches;
    }
}
