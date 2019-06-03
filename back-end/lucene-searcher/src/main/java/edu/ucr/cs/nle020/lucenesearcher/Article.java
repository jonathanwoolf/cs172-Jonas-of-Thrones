package edu.ucr.cs.nle020.lucenesearcher;

public class Article {

    public int id;
    public String title;
    public String body;

    public Article(){}

    public Article(int id, String title, String body) {
        this.id = id;
        this.title = title;
        this.body = body;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    @Override
    public String toString() {
        return String.format("Article[id=%d, title=%s, body=%s]", id, title, body);
    }
}
