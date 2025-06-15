#!/usr/bin/env python3
"""
🎯 المحرك الأساسي لنظام التنبؤ بالأعداد الأولية المصفوفي
Matrix-Based Prime Prediction System - Core Engine
"""

def predict_next_prime(current):
    """التنبؤ بالعدد الأولي التالي"""
    candidate = current + 2 if current % 2 == 1 else current + 1
    
    while candidate < current + 1000:
        if is_prime_simple(candidate):
            return candidate
        candidate += 2
    
    return None

def is_prime_simple(n):
    """فحص بسيط للأولية"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    print("🎯 اختبار المحرك الأساسي")
    test_cases = [13, 17, 29, 97, 113]
    
    for num in test_cases:
        result = predict_next_prime(num)
        print(f"العدد الأولي بعد {num}: {result}")
