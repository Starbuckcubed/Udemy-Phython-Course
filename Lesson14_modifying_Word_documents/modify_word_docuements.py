import docx

docpath1 = "word_documents/panda1.docx"
docpath2 = "word_documents/panda2.docx"

doc1 = docx.Document(docpath1)
doc2 = docx.Document(docpath2)

#extracts the 1st paragraph in the second document to a string
#preserves font and color because we used a paragraph element instead of the text element
para = doc2.paragraphs[0]

#extract a list of paragraphs within the first document with this expression
paragraphs = doc1.paragraphs
#access the second paragraph
#after the second paragraph add the new paragraph
paragraphs[1]._element.addnext(para._element)
doc1.save("word_documents/panda.docx")