package org.example.design.aop;

import org.example.design.proxy.Html;

public class  AopProxy implements IAopBrowser{

    private String url;
    private Html html;
    private Runnable before;
    private Runnable after;

    public AopProxy(String url){
        this.url = url;
    }

    public AopProxy(String url, Runnable before,  Runnable after) {
        this.url = url;
        this.before = before;
        this.after = after;
    }

    @Override
    public Html show() throws InterruptedException {
        after.run();

        if(html == null){
            this.html = new Html(url);
            System.out.println("BrowserProxy loading html from "+url);
        }
        System.out.println("BrowserProxy use cache html");
        Thread.sleep(2000);
        before.run();
        return html;
    }
}
