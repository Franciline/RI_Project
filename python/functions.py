# functions to load the files

import numpy as np 

# forma first element
def parse_car_header(obj):
    return {
        "format": obj[0],             
        "version": obj[1][0],         
        "corpora": [
            {
                "id": x[1],
                "lang": x[2],
                "source": x[3]
            }
            for x in obj[2][1]
        ],
        "dataset": obj[2][2]
    }

def parse_topic(node):
    """
    Recursively parse CAR topic tree
    """
    level = node[0]
    title = node[1]
    topic_id = node[2].decode("utf-8") if isinstance(node[2], bytes) else node[2]

    children = []

    # node[3] contains subtopics
    for child in node[3]:
        children.append(parse_topic(child))

    return {
        "level": level,
        "title": title,
        "id": topic_id,
        "children": children
    }

def parse_all_topics(raw_topics):
    return [parse_topic(t) for t in raw_topics]