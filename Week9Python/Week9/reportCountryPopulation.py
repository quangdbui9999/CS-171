user_input = input()
entries = user_input.split(',')
country_pop = dict(pair.split(':') for pair in entries)
# country_pop is now a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }
# Input: China:1365830000,India:1247220000,United States:318463000,Indonesia:252164800
''' Your solution goes here '''
for country, pop in country_pop.items():
    print(country, 'has', pop, 'people.')