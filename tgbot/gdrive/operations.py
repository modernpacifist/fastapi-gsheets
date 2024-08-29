from datetime import datetime


def get_folder_files(conf, parent_folder_id, folder):
    try:
        folder_id = (
            conf.sacc.files()
            .list(q=f"'{parent_folder_id}' in parents and name='{folder}'",
                  pageSize=10,
                  spaces='drive',
                  fields="files(id)")
            .execute()
        ).get('files')[0].get('id')

        fetched_files = (
            conf.sacc.files()
            .list(q=f"'{folder_id}' in parents",
                  pageSize=10,
                  spaces='drive',
                  fields="nextPageToken, files(id,name,createdTime,webViewLink)")
            .execute()
        )
        files = fetched_files.get('files')
        for f in files:
            # print(f.get('createdTime'))
            d = datetime.strptime(f.get('createdTime'), "%Y-%m-%dT%H:%M:%S.%fZ")
            print(d)

        return fetched_files.get('files')

    except Exception as e:
        print(e)
        return None
