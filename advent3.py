def organizeInventory(inventory):
  # Code here
  dict= {}
  for item in inventory:
    if (item['category'] not in dict.keys()):
        dict[item['category']]={item["name"]:item["quantity"]}
    else:
        if (item["name"] not in dict[item['category']].keys()):
            dict[item['category']][item["name"]]=item["quantity"]
        else:
             dict[item['category']][item["name"]]+=item["quantity"]
  return dict