# Privacy-Aware Speech Recognition

The Privacy-Aware Speech Recognition (PSR) aims to recognize and translate spoken language into text through computational linguistics in a privacy-preserving way. The analytic performs a speech-to-text process, listening to audio signal and delivering an editable and verbatim transcription of the speeches present in an audio signal where the sensitive information have been anonymized. When required, a privacy preserving version of the original audio can be obtained back as well by simply performing a text-to-speech translation of the anonymized text result. The produced privacy preserving transcriptions and audio can be then sent to external service since they don’t reveal any sensitive information.

The Privacy-Aware Speech Recognition needs as input data an audio sample containing a voice to translate. An audio sample compatible with the current implementation of the analytic should have a sampling rate of 16000Hz, with 1 single channel (mono) represented in 16 bit. Such an audio sample can be captured by any device and, in the case of different audio formats, a pre-processing step should be performed to adapt the audio sample to the mentioned input analytic format. Moreover, audio streaming is also applicable, as the python module is also capable of recording audio streams to be recognized.

## Files in this directory are as below:
- **First File "Text_to_Speech.py"**: For converting tesxt to speech.
- **Second File "deep_streaming.py"**: For privacy-aware speech recognition using an audio stream.
- **Third File "deep_wavFile.py"**: For privacy-aware speech recognition using an audio file.
- **Fourth File "record_audio.py"**: For recording audio.


## License

Released under the [MIT License](LICENSE).

## Acknowledgements

This software has been developed in the scope of the H2020 project SIFIS-Home with GA n. 952652.
