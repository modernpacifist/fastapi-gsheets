# def _get_overall_info(conf):
#     try:
#         return (
#             conf.sacc.files()
#             # .list(pageSize=10, fields="nextPageToken, files(id, name)")
#             .list(pageSize=10, fields="files(id, name)")
#             .execute()
#         )

#     except Exception as e:
#         print(e)
#         return None


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
                  fields="nextPageToken, files(id,name,webViewLink)")
            .execute()
        )

        return fetched_files.get('files')

    except Exception as e:
        print(e)
        return None
