from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

# جلب المفتاح من نظام التشغيل (لحماية مفتاحك من السرقة عند رفع الكود)
API_KEY = os.getenv("GEMINI_API_KEY")

# إعداد العميل (Client)
# إذا كنت تجرب الكود محلياً قبل ضبط "Environment Variable"، 
# يمكنك وضع المفتاح مؤقتاً هنا بدلاً من os.getenv، لكن احذفه قبل الرفع!
client = genai.Client(api_key=API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        user_input = data.get('message')

        # استخدام موديل Gemini 3 Flash الجديد
        response = client.models.generate_content(
           # تأكد من استخدام هذا الاسم تحديداً للموديل
model = genai.GenerativeModel('gemini-3-flash')
            contents=user_input
        )
        
        return jsonify({'response': response.text})
    
    except Exception as e:
        # طباعة الخطأ في التيرمينال للمساعدة في التشخيص
        print(f"Error details: {e}")
        return jsonify({'response': "عذراً، حدث خطأ في معالجة طلبك. تأكد من إعداد المفتاح بشكل صحيح."})

# إعدادات التشغيل لتناسب السيرفرات العالمية (مثل Render)
if __name__ == '__main__':
    # host='0.0.0.0' تسمح بالوصول للتطبيق من خارج جهازك
    port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    if __name__ == "__main__":
    # هذا السطر يخبر التطبيق أن يعمل على البورت 8000 الذي يطلبه Koyeb
    app.run(host='0.0.0.0', port=8000)    