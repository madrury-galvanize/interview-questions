# Case Studies

These questions are open ended case studies.  The goal here is to have a dialogue with the student (interviewee) about methodologies and techniques to solve the problem.

## Calender App

You are working for a large software company that provides a calendering application to large businesses.  The businesses use the application to schedule all meetings between employees.

Your company would like to learn more about how the customers are using the application, and in particular, are interested in how users with different profiles interact with the application.  As a small part of this project, you must identify which users of the application within a company are managers.

Assume you have access to all the scheduled meetings at a large company across multiple years.  Each data record you have available represents one meeting scheduled at this company, and contains the following information:

  - A user id for the person who scheduled the meeting.
  - User id's for all the people invited to the meeting.
  - A timestamp for the time the meeting began.
  - A timestamp for the time the meeting ended.
  - A flag for whether the meeting is recurring (i.e. an instance of a repeating meeting that recurs at regular time intervals).
  - Information on the recurrence of a meeting (i.e. is the meeting weekly, monthly, quarterly...).

You have no other information; in particular, you have no identifying features about the users of the application besides the meetings they were invited to or scheduled.

Discuss how you would design a solution for identifying the users within the organization that are managers.


## Library Project

You are contracted with a large public library (which has multiple locations within a US metro area) to help identify checkouts of books that are at a high risk of not being returned.  You have five years of historical data in three tables (this data will be pulled for you on the day the contract begins, and will be current up to that day):

#### Users

| column    | type    |
|-----------|---------|
| user_id   | int     |
| join_date | date    |
| branch_id | int     |
| name      | string  |
| ...       | ...     |

#### Books

| column       | type   |
|--------------|--------|
| book_id      | int    |
| author_id    | int    |
| genere_id    | int    |
| publish_date | date   |
| name         | string |
| ...          | ...    |

#### Checkouts

| column        | type      |
|---------------|-----------|
| user_id       | int       |
| book_id       | int       |
| checkout_time | timestamp |
| return_time   | timestamp |

The Users and Books table contain demographic style data on the users and books associated with the library, feel free to make assumptions about what exact information these tables may contain.  The `return_time` field in Checkouts table is `null` if the book has not yet been returned.

Discuss how you would develop a predictive model to help inform the library about what books are likely to go missing.  How would you deliver this data to the library?  How would you evaluate whether your solution meets the libraries needs?


## Insurance Pricing

You are a data scientist at a large car insurance company working on optimizing their pricing strategy.  Customers at this company pay for six month contracts; while the contract is in effect the company agrees to pay for all auto insurance losses incurred by the customer (for both accidents where the customer was and was not at-fault).  After a customer buys a contract at a given price, that contract cannot be re-priced, the insurance coverage is locked in for six months.  After the contract expires, your company will automatically offer the customer another six month contract, possibly with another price.

Your goal is to design a pricing strategy that will, on average, allow the company to stay profitable, and possibly, to accomplish this is an optimal way.

Discuss what data is important to collect on the insurance customers to accomplish this task.  What models are important to build, and what quantities are important to estimate?  How will these, possible multiple, models work in concert to form a full pricing strategy?


## Mailers for Churn


## Useful Forum Posts

## Reverse Case Studies
