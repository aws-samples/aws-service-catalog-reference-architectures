from pycalc import dot_prod

def lambda_handler(event, context):
    arr1 = event['arr1']
    arr2 = event['arr2']
    rval = dot_prod(arr1,arr2)
    return {"result":rval}
