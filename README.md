# htmldocx
Convert html to docx for export features namely the export tables with merge cells

Dependencies: `python-docx` & `bs4`

### Valispace version
There was a need to create a fork from this project for us to be able to fix an issue regarding the export of html tables with merge cells. To do that we used the code from an open [pull request](https://github.com/pqzx/html2docx/pull/45) in the main project. Once that PR is merged we can start using the main project again.

### To install

`pip install htmldocx`

### Usage

Add strings of html to an existing docx.Document object

```
from docx import Document
from htmldocx import HtmlToDocx

document = Document()
new_parser = HtmlToDocx()
# do stuff to document

html = '<h1>Hello world</h1>'
new_parser.add_html_to_document(html, document)

# do more stuff to document
document.save('your_file_name')
```

Convert files directly

```
from htmldocx import HtmlToDocx

new_parser = HtmlToDocx()
new_parser.parse_html_file(input_html_file_path, output_docx_file_path)
```

Convert files from a string

```
from htmldocx import HtmlToDocx

new_parser = HtmlToDocx()
docx = new_parser.parse_html_string(input_html_file_string)
```

Change table styles

Tables are not styled by default. Use the `table_style` attribute on the parser to set a table
style. The style is used for all tables.

```
from htmldocx import HtmlToDocx

new_parser = HtmlToDocx()
new_parser.table_style = 'Light Shading Accent 4'
```

To add borders to tables, use the `TableGrid` style:

```
new_parser.table_style = 'TableGrid'
```

Default table styles can be found
here: https://python-docx.readthedocs.io/en/latest/user/styles-understanding.html#table-styles-in-default-template

Change default paragraph style

No style is applied to the paragraphs by default. Use the `paragraph_style` attribute on the parser
to set a default paragraph style. The style is used for all paragraphs. If additional styling (
color, background color, alignment...) is defined in the HTML, it will be applied after the
paragraph style.

```
from htmldocx import HtmlToDocx

new_parser = HtmlToDocx()
new_parser.paragraph_style = 'Quote'
```

Default paragraph styles can be found
here: https://python-docx.readthedocs.io/en/latest/user/styles-understanding.html#paragraph-styles-in-default-template
