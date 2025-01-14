# Static Site Generator
<img src="ssg.jpg" width="256" alt="Static Site Generator">

[boot.dev](https://boot.dev) Static Site Generator

A python application that converts markdown files into html. The SSR script will first convert your markdown into html then setup a python http server for you to view the final result.

## Output

<img src="sample_html.png" width="256" alt="Sample HTML">

## Setup

Sample files are already included in this repository, but you can alter the content with these steps:

1. Build your markdown files representing your website content. These files should be markdown files (.md) and placed inside the `/content` folder.
2. Place all your static files into the `/static` folder. This should include any css and images.
3. (Optional) Edit the `template.html` to change the template that is used for the html.
4. (Optional) Edit the `main.sh` to further configure/alter the http server and edit `src/main.py` to change any of the folder locations should you choose to rename them.

## Usage

To start the website, simply run the main script:

```
./main.sh
```

The console will output the content files it converted to html and let you know the server is ready.

> Generating page from content/majesty/index.md to public/majesty/index.html using template.html
> Generating page from content/index.md to public/index.html using template.html
> Serving HTTP on 0.0.0.0 port 8888 (http://0.0.0.0:8888/) ...

Output is placed and served via the `/public` folder by default.

## Further Considerations

...
