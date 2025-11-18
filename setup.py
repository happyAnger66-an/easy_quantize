def main():
    setup(
        name="easy_quantize",
        version=get_version(),
        author="zhangxiaoan",
        author_email="zhangxiaoan@happyanger66.com",
        description="",
        long_description=open("README.md", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        keywords=["AI", "LLM", "GPT", "ChatGPT", "Llama", "Transformer", "DeepSeek", "Pytorch"],
        license="Apache 2.0 License",
        url="https://github.com/zhangxiaoan/easy_quantize",
        package_dir={"": "src"},
        packages=find_packages("src"),
        python_requires=">=3.9.0",
        install_requires=get_requires(),
        extras_require=extra_require,
        entry_points={"console_scripts": get_console_scripts()},
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
    )


if __name__ == "__main__":
    main()