SHORCUT TO STEP 6

1 - log in to developer account
2 - go to your apps and select the one you want
3 - write down the consumer key of the app
e.g.
M1SOKBXAEXAMPLEJOEXCTWWUSGN8RBUZ
4 - write down the callback url in "details" of the app
e.g.
http://localhost

now we will roughly follow the steps here. https://developer.tdameritrade.com/content/simple-auth-local-apps
5 - convert your consumer key and callback url to URL encoded text (you can use https://www.urlencoder.org/)
e.g.
M1SOKBXAEXAMPLEJOEXCTWWUSGN8RBUZ
http%3A%2F%2Flocalhost
6 - go to https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=URL_ENCODED_CALLBACK_URL&client_id=URL_ENCODED_CONSUMER_KEY%40AMER.OAUTHAP
e.g.
https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=http%3A%2F%2Flocalhost&client_id=M1SOKBEXAMPLEWUSGN8RBUZ%40AMER.OAUTHAP
7 - authenticate with user and password and you'll be directed to a 404 page, copy the URL there, something like
https://localhost/?code=5nTQaITyAZ9bdEJC%2B9PNIoxKZRBATwVSVoqOZHAH3560f7JgZ7ouqcjO3PEMYpZRgw9tsaBQDtZ4anpIrlZC93skWphKz497dPgOuZpwkncvZMSsgJ3EUTOJdelPHOd6he1gFjDgyOy9MJZvhnXPZUqFRM7GoPo%2BkDTQj1fG8bHo4TWRw2O50KeBWMPYT3nS3LbuBJoc6rmVZuSWJblbhuUoQnVtN%2FN%2BJlxG7AeCTycTbp0%2BBdRGoN%2B94GEnpRquVBc65PuuUjl9pE3884ug07Hpr0MjX8vttq78gcB7sffGytgDulEc7IbmBPLGPEy4tXZEXAMPLE81YPmH0%2BgZYFrF2f%2B0D%2B%2F0YTiGzzj7EK5EVE4vqj5ve%2BULr4iL638WUvMn%2BWV43QLr4WaEvSdG3ZwRox4RLlVRadDOsQB4DI5m00%2BWyMzMXlsYAMO100MQuG4LYrgoVi%2FJHHvlb2e0ZEIi0FxiglCiWpe3puEilPsClh1i6zR87ZJyi4U%2Ffubl9F8HTHwvA2kBacxTfbyp6ItRwRxqg1PDTWcoGsh4dOKANAv002orqhlERqMwwBQ5lnBHZpfGDYc43jbJQrzuYLtvIcR58sThrfOiIK08cg9%2FBI%2BznFPqKpAxc78HjWhOKFezdDghgFe%2B6otrf5WrKNkEYyRiNkCFQtL4n8iWjF%2BztJY1siV1Q7cdOICf6sVplkp1Lvo8nORkb1RTIvlnlgGJrZ3hIMF9yE9JCt2%2FmgtgmgUD%2Bvo%2Bo2br9fHM9141clFJajHf6VKNhpc6ymGB%2FL%2BsvHsfYvCrDsff8JoNPrH64pHrp1GpCcgFNV3dCyc6hjBgBEzQyckk4Z71oS80OTlR0WtVrGGU0qUSPkXmZqWT65dDdIYIs4XmkxrQlagq606%2FhSChFBg%3D212FD3x19z9sWBHDJACbC00B75E


8- url decode whatever is after "code=", something like
5nTQaITyAZ9bdEJC+9PNIoxKZRBATwVSVoqOZHAH3560f7JgZ7ouqcjO3PEMYpZRgw9tsaBQDtZ4anpIrlZC93skWphKz497dPgOuZpwkncvZMSsgJ3EUTOJdelPHOd6he1gFjDgyOy9MJZvhnXPZUqFRM7GoPo+kDTQj1fG8bHo4TWRw2O50KeBWMPYT3nS3LbuBJoc6rmVZuSWJblbhuUoQnVtN/N+JlxG7AeCTycTbp0+BdEXAMPLEGEnpRquVBc65PuuUjl9pE3884ug07Hpr0MjX8vttq78gcB7sffGytgDulEc7IbmBPLGPEy4tXZfxNjsPl81YPmH0+gZYFrF2f+0D+/0YTiGzzj7EK5EVE4vqj5ve+ULr4iL638WUvMn+WV43QLr4WaEvSdG3ZwRox4RLlVRadDOsQB4DI5m00+WyMzMXlsYAMO100MQuG4LYrgoVi/JHHvlb2e0ZEIi0FxiglCiWpe3puEilPsClh1i6zR87ZJyi4U/fubl9F8HTHwvA2kBacxTfbyp6ItRwRxqg1PDTWcoGsh4dOKANAv002orqhlERqMwwBQ5lnBHZpfGDYc43jbJQrzuYLtvIcR58sThrfOiIK08cg9/BI+znFPqKpAxc78HjWhOKFezdDghgFe+6otrf5WrKNkEYyRiNkCFQtL4n8iWjF+ztJY1siV1Q7cdOICf6sVplkp1Lvo8nORkb1RTIvlnlgGJrZ3hIMF9yE9JCt2/mgtgmgUD+vo+o2br9fHM9141clFJajHf6VKNhpc6ymGB/L+svHsfYvCrDsff8JoNPrH64pHrp1GpCcgFNV3dCyc6hjBgBEzQyckk4Z71oS80OTlR0WtVrGGU0qUSPkXmZqWT65dDdIYIs4XmkxrQlagq606/hSChFBg=212FD3x19z9sWBHDJACbC00B75E

9 - go to https://developer.tdameritrade.com/authentication/apis/post/token-0

10 - fill out values

grant_type: authorization_code
access_type: offline
client_id: {Consumer Key} (e.g. M1SOEXAMPLERBUZ@AMER.OAUTHAP)
redirect_uri: {REDIRECT URI} (e.g. http://localhost)
11 - fill out "code" with what came out in step 8 
12 - hit SEND
13 - copy output
14 - paste in `credentials/credentials.json`
 



