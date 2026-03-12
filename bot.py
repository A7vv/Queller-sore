import subprocess
import os

def update_store():
    try:
        print("🚀 جاري بدء تحديث المتجر تلقائياً...")
        # جلب أي تغييرات من GitHub لتجنب الأخطاء
        subprocess.run(["git", "pull", "origin", "main", "--rebase"], check=True)
        # إضافة كل ملفاتك الجديدة (مثل index.html)
        subprocess.run(["git", "add", "."], check=True)
        # حفظ التعديلات
        subprocess.run(["git", "commit", "-m", "تحديث من البوت الذكي"], check=True)
        # الرفع النهائي للموقع
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("\n✅ مبروك! تم تحديث متجرك بنجاح.")
    except Exception as e:
        print(f"\n❌ حدث خطأ: {e}")

if __name__ == "__main__":
    update_store()