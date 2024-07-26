const PDFExtract = require('pdf.js-extract').PDFExtract;
const pdfExtract = new PDFExtract();
const options = {}; /* see below */
let string = '';
pdfExtract.extract('coverletter.pdf', options, (err, data) => {
  if (err) return console.log(err);
  const strObj = data.pages[0]['content']
  for( let obj of strObj){
      string += obj['str']
    }
});
