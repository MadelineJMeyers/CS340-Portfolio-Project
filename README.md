# CS340-Portfolio-Project

### How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

I create programs incrementally, first I idenitfy what cases I need to create which in this case was a CRUD module and thus I knew I would need a Create, Read, Update, and Delete functionality for this program. Next, I reference what I will be using to work with the program, in this case I was using MongoDB and my module would need to work with it and so I referenced what each of these functions look like with MongoDB and translated them into Python. I then test my program to make sure the functionality is working correctly which helps me to understand what I may be missing.

To help with readability I make sure to adhere to best coding practices so that anyone who would be reading my code will be able to easily understand it and I make sure to add comments which directly state the functionality of sections of the code both for myself and anyone who may be working with the code in the future.

To help with adaptability, I make sure to use variables to work with sections that may need to be set for different systems. In this module I used variables to work with the Mongo Host and Port as well as the Username and Password which can be easily modified to work with different systems.

Each of these elements help me to create well constructed programs and allow me to create programs that can be used in different environments with little issues.

For instance, if I needed to use this module to work with a different web dashboard program I would be able to easily edit small sections of the code to make it work.

### How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

My main approach is to listen to my clients and to make sure I have all of the details that they need for their program to work as they expect it to work. I take all of my work as seriously as possible and I have tried to use this approach with every assignement.

To create a new database I would most likely work from a datasheet program such as Excel to make sure that all of the fields are accounted for and the data will be properly organized for my client. Then I would import the datasheet into the database program to work with it as is required by my client.  


### What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists work with large amounts of data and are able to sort through it to find information and present it to their clients in a more understandable way. For instance, in this project I had a dataset that consisted of over 1000 entries of animals and included many that were unimportant to the assignment at hand. I was able to take this information and using information from my client to create filters to sort through the information I was able to narrow down this dataset into much smaller data chunks and then create graphs depicting the most important details of the information at hand. These graphs included a pie chart to show the distribution of animals that were relevant to their respective filters, a histogram to show a different method of grouping the information that could also be relevant to my client, and finally a geolocation chart based on the information from the database to show direct information that was very important to my client.

Because I was able to narrow down such a large amount of data and create detailed reports of the data I believe I would be able to help the company to not only find information that they needed quickly but also aid their selection of where to start with the information.

Without the information being worked through as thoroughly as I was able to provide in this assignment the information could have taken a lot longer for the client to examine and could have resulted in multiple deadends in their search for specific animals but because of my work I was able to create this information for them in a format that could be read quickly and results could be found within the time it took to load the dashboard and locate the filters they needed for their work.
