from config.environ import Environ
from connect.aws_session import AWSSession

# AWS_INFO
s3 = AWSSession.connector_cl('s3')


def get_materials_from_s3(bucket_name, prefix):
    materials_list = []
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    for content in response.get('Contents', []):
        if content['Key'].endswith('.csv'):
            material_url = f"https://{bucket_name}.s3.{Environ.AWS_REGION}.amazonaws.com/{content['Key']}"
            materials_list.append(material_url)

    return materials_list


if __name__ == '__main__':
    bucket_name = 'rawcommiditiesdata'
    prefix = 'commodities'
    a = get_materials_from_s3(bucket_name, prefix)[0]
    print(a)
    import pandas as pd
    df = pd.read_csv(a)
    # print(df)