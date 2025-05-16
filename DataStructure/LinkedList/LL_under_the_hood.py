head = {
    "value":11,
    "next": {
        "value": 3,
        "next": {
            "value": 33,
            "next":{
                "value":13,
                "next": None
            }
        }
    }
}

print(head['next']['next']['value'])
print(my_linked_list.head.next.next.value)