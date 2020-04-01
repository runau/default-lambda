import json
import common


def lambda_handler(event, context):
    common.helloWorld()
    return {
    'statusCode': 200,
    'body': json.dumps('hello lambda!', ensure_ascii=False)}
