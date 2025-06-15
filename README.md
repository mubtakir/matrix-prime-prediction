# 🔢 مولد الأعداد الأولية المتقدم
# Advanced Prime Numbers Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Stars](https://img.shields.io/github/stars/mubtakir/advanced-prime-generator?style=social)](https://github.com/mubtakir/advanced-prime-generator/stargazers)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Demo-yellow)](https://huggingface.co/spaces/Mubtakir/advanced-prime-generator)

## 🌟 جرب المشروع مباشرة

### 🚀 [**تجربة تفاعلية على Hugging Face**](https://huggingface.co/spaces/Mubtakir/advanced-prime-generator)
*لا يحتاج تثبيت - يعمل في المتصفح مباشرة*

---

## 📋 نظرة عامة

**العربية**: خوارزمية مبتكرة لإيجاد الأعداد الأولية باستخدام جدول ضرب الأعداد الفردية مع نظام غربال مقطعي متقدم ونظام تخزين مستمر.

**English**: An innovative algorithm for finding prime numbers using odd numbers multiplication table with advanced segmented sieve and persistent storage system.

## 🧮 الصيغة الرياضية الأساسية

```
P_n = {2} ∪ {p ∈ O_n : p ∉ C_n ∧ p > 1}
```

حيث:
- **O_n**: مجموعة الأعداد الفردية `{x ∈ ℕ : x = 2k + 1, k ∈ ℕ₀, 1 ≤ x ≤ n}`
- **C_n**: مجموعة الأعداد المركبة الفردية `{x · y : x, y ∈ O_n, x ≥ 3, y ≥ x, x · y ≤ n}`
- **P_n**: مجموعة الأعداد الأولية حتى n

## ✨ المزايا الرئيسية

### 🚀 **الابتكارات التقنية**
- **توفير 50% من المساحة**: بتجاهل الأعداد الزوجية من البداية
- **غربال مقطعي متقدم**: حل مشكلة الذاكرة للأرقام الكبيرة
- **نظام تخزين مستمر**: حفظ الحالة والاستكمال من حيث توقف
- **دقة 100%**: نتائج مطابقة تماماً للطرق التقليدية

### 📊 **النتائج المثبتة**
| النطاق | الأعداد الأولية | الوقت | الدقة |
|--------|----------------|-------|-------|
| 100 | 25 | < 1s | ✅ 100% |
| 1,000 | 168 | < 1s | ✅ 100% |
| 10,000 | 1,229 | ~2s | ✅ 100% |
| 100,000 | 9,592 | ~30s | ✅ 100% |

## 🛠️ التثبيت والاستخدام

### التثبيت السريع
```bash
git clone https://github.com/mubtakir/advanced-prime-generator.git
cd advanced-prime-generator
```

### الاستخدام الأساسي
```bash
# التشغيل السريع - الأعداد الأولية حتى 1000
python run.py --quick 1000

# التشغيل التفاعلي
python prime_generator.py

# تشغيل الاختبارات
python run.py --test

# عرض الإحصائيات
python run.py --stats

# الأمثلة المتقدمة
python run.py --examples
```

## 📚 أمثلة سريعة

### مثال 1: الأعداد الأولية حتى 100
```bash
$ python run.py --quick 100
✅ تم العثور على 25 عدد أولي
🔢 النتيجة: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

### مثال 2: الاستكمال الذكي
```bash
$ python run.py --quick 1000  # المرة الأولى
✅ تم العثور على 168 عدد أولي حتى 1000

$ python run.py --quick 5000  # المرة الثانية
ℹ️ تم حساب الأعداد سابقاً حتى 1000، سأكمل من 1001 إلى 5000
✅ تم العثور على 669 عدد أولي حتى 5000
```

## 🔬 الميزات المتقدمة

### 🔄 **النظام المستمر**
- حفظ الحالة تلقائياً في `prime_state.json`
- استكمال من آخر نقطة توقف
- عدم تكرار الحسابات

### 📈 **التحليل المتقدم**
- **الأعداد الأولية التوأم**: البحث عن أزواج (p, p+2)
- **تحليل العوامل الأولية**: تفكيك الأعداد المركبة
- **اختبار حدسية جولدباخ**: تمثيل الأعداد الزوجية
- **إحصائيات مفصلة**: كثافة، فجوات، توزيع

### 📁 **التصدير المتعدد**
- **JSON**: للبيانات المنظمة
- **CSV**: للجداول والتحليل
- **TXT**: للقوائم البسيطة

## 🧪 التحقق من الصحة

### تشغيل الاختبارات الشاملة
```bash
python test_prime_generator.py
# ✅ 10/10 اختبارات نجحت
# ✅ مطابقة 100% مع الطرق التقليدية
```

### مقارنة الأداء
```bash
python run.py --compare 1000
# مقارنة تلقائية مع غربال إراتوستينس التقليدي
```

## 📖 التوثيق الشامل

### للمبتدئين
- **[`QUICK_START.md`](QUICK_START.md)**: بداية سريعة في 3 خطوات
- **[`USER_GUIDE_SIMPLE.md`](USER_GUIDE_SIMPLE.md)**: دليل مفصل للمبتدئين

### للمتقدمين
- **[`SCIENTIFIC_REPORT.md`](SCIENTIFIC_REPORT.md)**: تقرير علمي شامل
- **[`FAQ_MATHEMATICIANS.md`](FAQ_MATHEMATICIANS.md)**: أسئلة شائعة للرياضيين
- **[`PROJECT_SUMMARY.md`](PROJECT_SUMMARY.md)**: ملخص المشروع النهائي

## 🎯 التطبيقات

### للرياضيين
- دراسة توزيع الأعداد الأولية
- اختبار الحدسيات الرياضية
- تحليل الأنماط العددية

### للباحثين
- نظرية الأعداد
- التشفير والأمان
- تطوير الخوارزميات

### للمطورين
- مثال على تطوير الخوارزميات
- تقنيات تحسين الأداء
- أنماط التصميم البرمجي

## 📊 مقارنة مع الطرق التقليدية

| الخاصية | غربال إراتوستينس | **الطريقة المقترحة** |
|---------|------------------|---------------------|
| **استهلاك الذاكرة** | O(n) | **O(√n)** |
| **قابلية التوسع** | محدودة | **لانهائية نظرياً** |
| **الاستمرارية** | لا | **✅ نعم** |
| **توفير المساحة** | 0% | **✅ 50%** |
| **الدقة** | 100% | **✅ 100%** |

## 🏗️ هيكل المشروع

```
advanced-prime-generator/
├── 📄 الوثائق الأساسية
│   ├── README.md                    # هذا الملف
│   ├── SCIENTIFIC_REPORT.md         # التقرير العلمي
│   ├── USER_GUIDE_SIMPLE.md         # دليل المبتدئين
│   └── FAQ_MATHEMATICIANS.md        # أسئلة شائعة
│
├── 🐍 الملفات البرمجية
│   ├── prime_generator.py           # الخوارزمية الأساسية
│   ├── run.py                       # واجهة التشغيل السريع
│   ├── examples.py                  # أمثلة متقدمة
│   ├── test_prime_generator.py      # اختبارات شاملة
│   └── app.py                       # واجهة Gradio
│
├── ⚙️ ملفات الإعداد
│   ├── setup.py                     # إعداد التثبيت
│   ├── requirements.txt             # متطلبات المشروع
│   └── config.py                    # إعدادات النظام
│
└── 📜 ملفات أخرى
    ├── LICENSE                      # رخصة MIT
    ├── CHANGELOG.md                 # سجل التغييرات
    └── .gitignore                   # ملفات Git المتجاهلة
```

## 🤝 المساهمة

نرحب بالمساهمات! إليك كيفية المساهمة:

1. **Fork** المشروع
2. إنشاء **فرع جديد** (`git checkout -b feature/amazing-feature`)
3. **Commit** التغييرات (`git commit -m 'Add amazing feature'`)
4. **Push** للفرع (`git push origin feature/amazing-feature`)
5. إنشاء **Pull Request**

### أنواع المساهمات المرحب بها:
- 🐛 إصلاح الأخطاء
- ✨ ميزات جديدة
- 📚 تحسين التوثيق
- 🎨 تحسين الواجهة
- ⚡ تحسين الأداء

## 🔮 خطط التطوير المستقبلية

### قريباً
- [ ] واجهة رسومية سطح المكتب
- [ ] معالجة متوازية
- [ ] تحسينات الأداء

### متوسط المدى
- [ ] API ويب RESTful
- [ ] تطبيق ويب متقدم
- [ ] تكامل قواعد البيانات

### طويل المدى
- [ ] تطبيق الهاتف المحمول
- [ ] حوسبة سحابية
- [ ] ذكاء اصطناعي للتنبؤ



## 👨‍💻 المؤلف

**مبتكر (Mubtakir) باسل يحيى عبدالله**
- 🐙 GitHub: [@mubtakir](https://github.com/mubtakir)
- 🤗 Hugging Face: [@Mubtakir](https://huggingface.co/Mubtakir)
- 📧 البريد الإلكتروني: mubtakir@example.com


## 🌟 إذا أعجبك المشروع

إذا وجدت هذا المشروع مفيداً، يرجى:
- ⭐ إعطاء نجمة للمستودع
- 🍴 عمل Fork للمساهمة
- 📢 مشاركة المشروع مع الآخرين
- 🐛 الإبلاغ عن الأخطاء أو اقتراح تحسينات

---

**"الرياضيات هي لغة الكون، والأعداد الأولية هي ذراتها الأساسية"**

*"Mathematics is the language of the universe, and prime numbers are its fundamental atoms"*
