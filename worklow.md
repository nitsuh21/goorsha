#modules
1. Affiliate marketing
=> companies post an add with affiliate link
=> users copy that link
=> users lead/trafick is tracked with that link

#models
1. users
- Full name
- Address
- Business - one to many
- socials - (telegram)

2. Business
- Name
- Address 
- Owner - Foreignkey
- Managers - MtoM with users
- No of Customers/ Followers - M to M with users
- Campaign - one to many with Campaign

3. Campaign
- Name
- Target
- Affiliates - Many to Many with users
- current 

4. post/blog
- title
- slug
- content
- images

5. contract
- issuedby - one to one
- issuedfor - one to one
- contact