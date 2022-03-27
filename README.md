# Election Analysis - John Morrissey 

## Overview of Audit
The purpose of this audit is to verify the votes for three counties were counted accurately and the right candidate elected. Data is broken down into total votes by county and candidate. This data can later be compared to general election data to identify whether there are discrepancies. Audits are commonly used in very close elections, but for this particular dataset this is not the case. The analysed data can also be compared to past election data to identify any potential issues. 

## Election Audit Results 

For this audit the data was collected into a CSV file. Python was then used to pull the file and analyze the data. For loops, conditional statements, lists, and dictionaries were used to go through the data row by row. The total number of votes, votes by candidate, and votes by county are tabulated. The script then prints the results in a readable format and declares the winning candidate. An election results file is created for future reference. The below image displays the results of the analysis. 

![Results of Analysis](resources/Results.png)

* From our analysis we found a total of 369,711 votes. 

* The county breakdown of votes are: 
    * Jefferson: 10.5% (38,855 votes) 
    * Denver: 82.8% (306,055 votes) 
    * Arapahoe: 6.7% (24,801 votes) 
    

* Denver County had the largest number of votes with 306,055 ballots cast. 

* Votes each candidate received are: 
    * Charles Casper Stockham: 85,213, 23% of total
    * Diana DeGette: 272,892, 74% of total
    * Raymon Anthony Doane: 11,606, 3% of total 

* Diana DeGette won the election with 272,892 total votes. She won 73.8% of votes cast. 


## Summary 

With slight modification this script has many uses beyond this analysis. The script will work with any county and candidate since the specific names are not directly coded in. While this election was a landslide, closer elections could benefit from an audit like this to ensure the candidates were elected fairly. The script can be expanded to compare results from previous elections by adding a date to the data. The script could be expanded to compare county votes from different years to give guidance on whether the amount of votes counted for the current election seem in line. A state column could also be added to allow for national elections. While fairly straightford, this script can easily be expanded upon to be a powerful tool for any election audit. 
