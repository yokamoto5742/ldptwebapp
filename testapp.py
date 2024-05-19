from fastapi import FastAPI, Response
from reportlab.pdfgen import canvas
import io

app = FastAPI()

@app.get("/download_pdf")
async def download_pdf():
    # PDFファイルを生成する
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello, PDF!")
    p.showPage()
    p.save()

    # バイトストリームを先頭に戻す
    buffer.seek(0)

    # レスポンスを作成し、ヘッダを設定する
    response = Response(content=buffer.getvalue(), media_type="application/pdf")
    response.headers["Content-Disposition"] = "attachment; filename=example.pdf"

    return response
