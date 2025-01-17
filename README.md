# EmailAdapter
A simple adapter for email automation with python.

## Features
| Email Provider | Login | Register | Send Email | Read Inbox |
| -------------- | ----- | -------- | ---------- | ---------- |
| Freemail.hu    | |:heavy_check_mark: 
| Gmail.com      | 
| proton.me      | 
| GuerrillaMail  | 

## Download

Just copy the code below to download the module

```
git clone --no-checkout https://github.com/balintkeri/EmailAdapter.git
cd EmailAdapter
git sparse-checkout init --cone
git sparse-checkout set EmailAdapter/EmailAdapter
git checkout
```

## Usage
Dependency : Selenium and Python 3

```
import datetime
import EmailAdapter

adapter = EmailAdapter.Freemail()
adapter.register(
    "emailBody",
    "lastName",
    "firstName",
    "password",
    "secureAnswer",
    datetime.date(1999,1,1)
)
```
