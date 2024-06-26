#!/usr/bin/env python3
'''Module provides stats on NGINX logs'''

import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["logs"]

nginx_col = db["nginx"]

all_logs = nginx_col.count_documents({})
print(f"{all_logs} logs")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {}
for method in methods:
    cnt = nginx_col.count_documents({"method": method})
    method_counts[method] = cnt
print("Methods:")
for method, cnt in method_counts.items():
    print(f"    method {method}: {cnt}")

spec_method = "GET"
spec_path = "/status"
spec_count = nginx_col.count_documents(
        {"method": spec_method, "path": spec_path})
print(f"{spec_count} status check")

pipeline = [
    {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
]

res = nginx_col.aggregate(pipeline)
print("IPs:")
for doc in res:
    print(f"    {doc['_id']}: {doc['count']}")
