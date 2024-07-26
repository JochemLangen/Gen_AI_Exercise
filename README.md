# Generative AI Recruitment Assignment

Congratulations on getting through the first interview round!

There are two steps remaining, this assignment and if needed a second interview. During that interview, we will discuss your assignment submission and any outstanding interview or practical questions. 

We are looking for someone with a technical / science background, good collaboration and communication skills, knowledge of artificial intelligence (preferably incl. Natural Language Processing) and experience with prompt engineering. The main goal of the internship is the following:
- Learn about ASML and immerse yourself in the work being done within Metrology
- Gather and come up with use-cases for our in-house or subscribed Gen. AI tools, given the development processes within our department
- Test how we can implement these tools best for each process / use-case
- Develop a usage guide and template (and potentially look into efficiency gains)
- Provide feedback on these tools and suggest additional products or features needed for other usecases that don't work with the current products
- Depending on the available time, results of the internship and budget, we may even move onto implementing and contributing to new tools        

The processes that we would apply these tools to include but are not limited to:
- Data manipulation
- Analysis script writing
- Lithography machine calibration model and software development 
- Lithography machine simulations
- Requirements engineering
- Communication
- Documentation and presentations

You will be mentored by a Functional Design Engineer from the Metrology department (Jochem Langen) who will teach you about ASML, the metrology technical context and details of our work as well as guiding you through the project.    
Furthermore, you will have contact with a lot of other engineers within our cluster, all with potentially different use-cases. As part of your introduction to our AI tools and to provide additional support with testing if needed, you will also interact with our AI innovation lab. This team of AI engineers have worked on developing the Gen. AI tools or are involved in the intake process of external ones. They will also be looking for feedback on how their products can be improved.

## Asignment: The Grumpy Fruit Inspector
For this assignment you will be using the base ChatGPT-4 model (https://chatgpt.com/) to generate a random selection of fruit baskets with randomly ordered fruit, from apples and oranges to blueberries and strawberries! You need to write a **single** prompt that generates the content of a fruit baskets file as output (not just a python script). An example of a shorter version of the file you will be creating is stored in ./data/fruit_baskets_example. Whether your baskets are valid will be tested by the fruit inspector. First run this file: ./code/fruit_inspector.py and then you can test your files by initialising the fruit inspector class or by using its functions. Save your prompt and the resulting plot in a word or pdf file.

Whilst the fruit inspector tries to be thorough, they don't like following all programming guidelines. Write a **single** prompt that improves the documentation in fruit_inspector.py, from function descriptions with information about input and output, to short descriptions in-between the code to describe the functionality. Save your prompt in a text file or pdf and save the new version of ./code/fruit_inspector.py.

After the inspector approved your fruit today, you are not sure if you will have enough fruit for him tomorrow. So, instead, you need to fool him by making him re-inspect today's fruit by thinking it's different! Create a **single** prompt that reshuffles the boxes in your file and the fruit inside each box. It must not change the number of each box type or the fruit inside the boxes, just the order. Save your prompt and the resulting plot in a word or pdf file.

(BONUS)
The fruit inspector is ambitious and wants to check how random the fruit baskets really are. Create a **single** prompt that adds a function to the fruit_inspector class. Given input on the population probability of each type of basket and each type of fruit within those baskets, the function should output what the probability is that the total number of each basket and each fruit type in the fruit basket file adheres to these probability distributions. For the fruit types, this should take into account how many baskets of the appropriate type there are in the file. In other words, if the baskets in the file are deemed likely not to be following the distribution, the fruit types still can be and vice-versa. Save your prompt in a text file or pdf and the new version of ./code/fruit_inspector.py.

Your results will be evaluated on the following:
- Demonstrated understanding of the exercise
- Effort put in
- Quality of the results
- Robustness of the prompts (does the prompt produce a similar quality result each time)
- Clarity and thoroughness of the python scripts and their documentation
- Clarity of any additional documentation you provide about any assumptions you made

Note, the prompt for each exercise should be fully independent and not require the context of the previous prompts.

Please send your results to [jochem.langen@asml.com](mailto:jochem.langen@asml.com), [jonathan.deweirdt@asml.com](mailto:jonathan.deweirdt@asml.com) & [georg.wilding@asml.com](mailto:georg.wilding@asml.com). Please put the results of each exercise in a separate folder and attach all of them together in a zipped folder.

## Deadline
The assignment should be should be handed in by 23:59 pm on Wednesday the 7th of August. If an additional interview will be needed we would be looking to have those the week after (12th - 18th of August).
If for some reason you will not be able to complete the assignment before the deadline, please let me know via: [jochem.langen@gmail.com](mailto:jochem.langen@gmail.com) (note this is a different email than used above).
