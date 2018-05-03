import markdown
import codecs


def convertMDtoHTML(fileurl = None):
     f = codecs.open(fileurl, "r",
                          encoding="utf-8",
                          errors="xmlcharrefreplace"
                    )
     contents = f.read()
     html = markdown.markdown(contents)
     print(html)
     return html

