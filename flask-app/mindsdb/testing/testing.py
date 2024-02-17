import mindsdb_sdk

# connects to the default port (47334) on localhost 
server = mindsdb_sdk.connect()

# connects to the specified host and port
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

files = server.list_databases()[0]
credentials = files.query('SELECT * FROM google_credentials').fetch().loc[0]['installed']
server.create_database('mindsdb_gmail', 'gmail', 
                       {"s3_credentials_file": "https://aihacks-google-credentials.s3.us-west-1.amazonaws.com/google_credentials.json?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLWVhc3QtMiJIMEYCIQD20rTJxiFXTZGIDV06CklDGK%2B0cX7Rs%2FrDT0DlbpncrgIhALckLyKjc3aR5DB0nMQVoZUbQ4a33q%2FYC7u86%2FM7ysD%2BKugCCHEQABoMMzcyNDAzMjEzMzE1IgwkVlkL6lJkCpcEyCwqxQIt%2FkuAJy%2FYH93ajnpdbgsRuL4W%2FqkWZWmqghp5kRaTnn0NYpnmShzvUWd4tx4ryE%2FACzcL7ZPWbPqLVbvbjjZGt%2FTWEirf%2FVpOo5zcU%2B3mbTOSiGkx6u%2BH9fnK3iSPC0bli8BBh8hapN1POv%2FDHGQG6BHsQlKKnqMcL8MZJmpN7%2FiSbLjxaaD%2Bdju%2BidZAL6sE7pDZCHOEdOlqdGUAfvsauJCX4RmZEyFJD%2B1%2BU0ligUcIgc3SUUQqEZH5QJkrdfjevulhAUI8H0J6JWg7rgQunQ7Q4J82seXNQmdz6r%2Bb0hE%2FQdLUrccvDCYv5vqOygYv6yMQLrGTButY60SABiVAdCUqYer43rPmSa9C9ef3OKIioExIG7NNVh8sEkY%2BpLLKolSd9U%2FK8EeJ23hwLgSB%2FlRbq60TOVJ3BId47BXZubmPZSWPMKbouqQGOrICcLiwTyYdvMApWhu2iZSvPRUDGSBdVrtLXKqdsP1zAoVvWY0KII%2FUarX3nIz026ucHR9cu5iOxqxLdEMio3f8QavcyTmmxKK0b9l%2F2qzEGXaSaXp5%2FE%2B1a2LegkL%2B8zhlaVZNVnknmH0Tb7a61eUe3%2FZNqlh6eK1zY3VWen5YbYaZlKXGUJaFaiek4gtQwdLIhZIvca%2FKR3zbqaEIlWoBeFLSj4x9JSlc34aI%2FIu2siaOv5%2FlHANhwcGcITJX%2B%2FeNStluSOae5yVllqKBPotyisuQWbP6c7jmtgxwyvH3QBeIepnsKA6AKFznBFJQosJufU8mEnVsqIgIj5Jgn1oupkctv6aAjhZgiuFgP563EPUTl6CUwAnr9np0%2BKSELDrjhIXFP2X6nHCOn%2F9Bqm8ppglo&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230618T074121Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAVNNHWCQBSXYT7HO5%2F20230618%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=ad8998fe76e252c43dee811eca3ea6db22173fdc9c005821b521d87864a59580",
                        "scopes": ['https://.../gmail.compose', 'https://.../gmail.readonly']}
                       )