FROM python:3.7.6
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN python -m pip install --upgrade pip
RUN pip install poetry

WORKDIR /Privacy_Preserving_Speech_Recognition
COPY pyproject.toml /Privacy_Preserving_Speech_Recognition

RUN poetry config virtualenvs.create false
RUN poetry install

RUN python -m spacy download en_core_web_sm

RUN curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
RUN curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

COPY deep_streaming.py /Privacy_Preserving_Speech_Recognition
COPY deep_wavFile.py /Privacy_Preserving_Speech_Recognition
COPY record_audio.py /Privacy_Preserving_Speech_Recognition
COPY sample1.wav /Privacy_Preserving_Speech_Recognition
COPY sample2.wav /Privacy_Preserving_Speech_Recognition
COPY sample3.wav /Privacy_Preserving_Speech_Recognition
COPY sample4.wav /Privacy_Preserving_Speech_Recognition

CMD \ 
	poetry run black --check . ; \
	poetry run pylint . ; \
	poetry run isort --check --diff . ; \ 
	poetry run flake8 ; \ 
	poetry run coverage run -m pytest deep_wavFile.py && poetry run coverage report -m