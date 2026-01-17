import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# 1. إعداد مفتاح الـ API من إعدادات السيرفر
# تأكد أنك سميت المتغير في Koyeb باسم GEMINI_API_KEY
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 2. استخدام موديل 1.5 flash لضمان السرعة والاستقرار
model = genai.GenerativeModel('gemini-1.5-flash-latest')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        user_message = data.get('message')

        if not user_message:
            return jsonify({'reply': 'الرجاء كتابة سؤال..'})

        # 3. إرسال السؤال للذكاء الاصطناعي
        response = model.generate_content(user_message)
        
        # التأكد من استلام نص
        if response.text:
            return jsonify({'reply': response.text})
        else:
            return jsonify({'reply': 'لم أستطع تكوين رد، حاول مرة أخرى.'})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'reply': f'حدث خطأ في الخادم: {str(e)}'})

if __name__ == "__main__":
    # تشغيل التطبيق على البورت 8000 كما يطلب Koyeb
    port = int(os.environ.get("PORT", 8000))
   if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))


