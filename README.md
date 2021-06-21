# swisstext-2021-task-3
Code to evaluate submissions for the SwissText 2021 Shared Task 3, "Swiss German Speech to Standard German Text".
1. Download the ground truth files private.csv and public.csv of the "All Swiss German Dialects Test Set" to the same directory as bleu.py. The test set is available here: https://www.cs.technik.fhnw.ch/i4ds-datasets
2. Copy the submission you want to evaluate to the same directory as bleu.py and rename it to submission.csv. Make sure the format is correct. Check the template example_submission.csv in the "All Swiss German Dialects Test Set".
3. Run bleu.py.
4. The first score is the BLEU score on the public part of the test set, the second score is the BLEU score on the private part.
