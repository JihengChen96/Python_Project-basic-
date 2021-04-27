email_input = str(input("enter your email "))

### .index("the text your want to index")
username = email_input[:email_input.index("@")]
domain_name = email_input[email_input.index("@")+1:]
format_ = (f"Your username is '{username}' and your domain is '{domain_name}'")
print(format_)