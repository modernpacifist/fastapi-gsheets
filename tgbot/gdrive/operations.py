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
        results = (
            conf.sacc.files()
            .list(q=f"'{parent_folder_id}' in parents and name='{folder}'",
                  pageSize=10,
                  spaces='drive',
                  fields="files(id)")
            .execute()
        )

        parent_folder_id = results.get()
        results = (
            conf.sacc.files()
            .list(q=f"'{parent_folder_id}' in parents and name='{folder}'",
                  pageSize=10,
                  spaces='drive',
                  fields="nextPageToken, files(id, name)")
            .execute()
        )

        # if folder:
        #     for f in results.get('files', []):
        #         if folder == f.get('name'):
        #             return f.get('id')
        #         # print()
        #     return results

        return results

    except Exception as e:
        print(e)
        return None
