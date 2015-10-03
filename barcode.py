__author__ = 'NAMIK'
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF

#----------------------------------------------------------------------
def createBarCodes():
    """
    Create barcode examples and embed in a PDF
    """
    c = canvas.Canvas("barcodes.pdf", pagesize=A4)

    barcode_value = "76651"


    # code93 also has an Extended and MultiWidth version


    x = 180 * mm
    y = 290 * mm
    x1 = 6.4 * mm

    code93.Standard93(barcode_value).drawOn(c, x, y)




    # draw a QR code
    qr_code = qr.QrCodeWidget('mailto:erdogannamik@gmail.com')
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(45, 45, transform=[45./width,0,0,45./height,0,0])
    d.add(qr_code)
    renderPDF.draw(d, c, 15, 45)

    c.save()

if __name__ == "__main__":
    createBarCodes()