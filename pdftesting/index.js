const express = require('express')
const fileUpload = require('express-fileupload')
const pdfParse = require('pdf-parse')

const app = express()

app.use('/',express.static('public'));
app.use(fileUpload());

function render_page(pageData) {
    //check documents https://mozilla.github.io/pdf.js/
    let render_options = {
        //replaces all occurrences of whitespace with standard spaces (0x20). The default value is `false`.
        normalizeWhitespace: false,
        //do not attempt to combine same line TextItem's. The default value is `false`.
        disableCombineTextItems: true
    }

    return pageData.getTextContent(render_options)
    .then(function(textContent) {
        let lastY, text = '';
        for (let item of textContent.items) {
            if(item.str === " ") console.log('thiss is item',item)
            if (lastY == item.transform[5] || !lastY){
                text += item.str;
            }
            else{
                text += '\n' + item.str;
            }
            lastY = item.transform[5];

        }
        return text;
    });
}
let options = {
    pagerender: render_page
}
app.post('/extract-text',(req,res)=>{
    if(!req.files && !req.files.pdfFile){
        res.status(400)
        res.end()
    }

    pdfParse(req.files.pdfFile).then(result=>{
        res.send(result.text)
    }).catch(e=>{
        res.status(403)
        res.end(e)
    })


})
app.listen(3000);
