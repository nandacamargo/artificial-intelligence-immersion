## Generate 10 reviews for movies 

Ask ChatGPT to generate 10 reviews for different movies, ask it to convert to CSV format 
and import to Google Sheets.
Use ChatGPT add-on inside the sheet to provide an expected grade for the movie, given the review.


## My Solution

### For the reviews - using ChatGPT - my prompts were:

Generate 10 reviews for great movies launched from 2010 to 2020. The output show have the name of the movie, the year and the review.

Generate 10 reviews for movies launched from 2010 to 2020. They should be a miscellaneous of good and bad reviews. The output show have the name of the movie, the year and the review


### For the grades - using SheetGPT plugin:

=GPT("From 0 to 10, what is the expected grade based on the review, The output should be a nummber" & C2)
