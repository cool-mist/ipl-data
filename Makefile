2023: .ipl-data/.c-install 2023/ipl-data-2023.pdf parse.py
	.ipl-data/bin/python parse.py 2023/ipl-data-2023.pdf 2023/ipl-data-2023.json

2023/ipl-data-2023.pdf:
	mkdir -p 2023
	curl https://documents.bcci.tv/bcci/documents/1676632383158_TATA%20IPL%202023%20-%20Match%20Schedule.pdf > 2023/ipl-data-2023.pdf

.ipl-data/bin/activate:
	python -m venv .ipl-data

.ipl-data/bin/pip-compile: .ipl-data/bin/activate
	.ipl-data/bin/python -m pip install pip-tools

requirements.txt: requirements.in .ipl-data/bin/pip-compile
	.ipl-data/bin/pip-compile --output-file=- > requirements.txt

.ipl-data/.c-install: requirements.txt
	.ipl-data/bin/pip install -r requirements.txt
	touch .ipl-data/.c-install

clean:
	rm -rf .ipl-data
	rm -rf __pycache__
	rm -rf requirements.txt
	rm -rf 2023/
