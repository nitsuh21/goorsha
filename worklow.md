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

#use cases
1. Sign up / social signup
- username
- email
- phonenumber
- password 
- pin

2. Sign in / social signin
- email + password
- pin

=> we gonna use DRF for this project. let's identify the correct approach for it.
- upon research made, applying JWT is choosen. because for stateless and no need to verify on db like token authentication


#How should the affiliate work?
currently let's add affiliates for products and introduce a new feature to add their services