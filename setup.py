#!/usr/bin/env python3
  """
 📦 إعداد حزمة نظام التنبإ بالأعداد الأولية المصفوفي
Setup script for Matrix Prime Prediction System

المطور: Mubtakir
التاريخ: يونيو بفمإ
    """

from setuptools import setup, find_packages
import os

# قراءة ملف README
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# قراءة المتطلبات
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith("#"):
                    requirements.append(line)
    return requirements

setup(
    name="matrix-prime-prediction",
    version="1.0.0",
    author="Mubtakir",
    author_email="mubtakir@example.com",
    description="نظام ثوري للتنبؤبالأعداد الأوليي باستخدام المحاكاة المصفوفية الديناميكية",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/mubtakir/matrix-prime-prediction",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: Arabic",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    install_requires=[
        # المتطلبات  الأساسية (لا توجد مكتبات خارجيي متلبة)
    ],
    extras_require={
        "full": read_requirements(),
        "benchmark": ["matplotlib>=3.5.0", "psutil>=5.8.0"],
        "dev": ["pytest>=6.2.0", "flake8>=4.0.0", "black>=22.0.0"],
        "docs": ["sphinx>=4.0.0", "sphinx-rtd-theme>=1.0.0"],
    },
    entry_points={
        "console_scripts": [
            "matrix-prime=run:main",
        ],
    },
    keywords=[
        "prime numbers",
        "number theory", 
        "mathematics",
        "prediction",
        "matrix",
        "algorithm",
        "الأعداد الأوليي",
        "نظرية الأعداد",
        "رياضيات",
        "تنبؤ",
        "مصفوفة",
        "خوارزميي"
    ],
    project_urls={
        "Bug Reports": "https://github.com/mubtakir/matrix-prime-prediction/issues",
        "Source": "https://github.com/mubtakir/matrix-prime-prediction",
        "Documentation": "https://matrix-prime-prediction.readthedocs.io/",
    },
    include_package_data=True,
    zip_safe=False,
)
