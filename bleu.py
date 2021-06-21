import csv
from os import path
import re
import sys
from typing import TextIO

from nltk.translate.bleu_score import corpus_bleu

ALLOWED_CHARS = {
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'ä', 'ö', 'ü',
    ' ',
}
WHITESPACE_REGEX = re.compile(r'[ \t]+')


def preprocess_transcript(transcript):
  transcript = transcript.lower()
  transcript = transcript.replace('ß', 'ss')
  transcript = transcript.replace('-', ' ')
  transcript = transcript.replace('–', ' ')
  transcript = WHITESPACE_REGEX.sub(' ', transcript)
  transcript = ''.join([char for char in transcript if char in ALLOWED_CHARS])
  transcript = WHITESPACE_REGEX.sub(' ', transcript)
  transcript = transcript.strip()

  return transcript
  
  
def split(transcript):
  return transcript.split(' ')


def score(submissionCsv: dict, privateCsv: TextIO):
  ref = []
  hyp = []
  reader = csv.reader(privateCsv, delimiter=',', quotechar='"')
  next(reader)  # This skips the header row of the CSV file.
  for row in reader:
    ref.append([split(preprocess_transcript(row[1]))])
    hyp.append(split(preprocess_transcript(submissionCsv.get(row[0]))))

  return corpus_bleu(ref, hyp)


if __name__ == '__main__':
  reader = csv.reader(open(path.join(path.dirname(sys.argv[0]), "submission.csv"), encoding="utf-8"), delimiter=',', quotechar='"')
  next(reader)  # This skips the header row of the CSV file.
  submissionCsv: dict = {rows[0]: rows[1] for rows in reader}

  privateScore = score(submissionCsv, open(path.join(path.dirname(sys.argv[0]), "private.csv"), encoding="utf-8"))
  publicScore = score(submissionCsv, open(path.join(path.dirname(sys.argv[0]), "public.csv"), encoding="utf-8"))
  print("%.20f" % publicScore, ";", "%.20f" % privateScore)
