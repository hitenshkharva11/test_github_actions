import looker_sdk

# Function to Get Looker Tiles Queries for a Dashboard
def get_dashboard_tile_queries(looker_sdk, dashboard_id):
    dashboard = looker_sdk.dashboard(dashboard_id)
    queries = []
    for element in dashboard.dashboard_elements:
        if element.look_id:
            look = looker_sdk.look(element.look_id)
            queries.append(look.query)
    return queries

# Function to Get All Looker Folders
def get_all_looker_folders(looker_sdk):
    all_folders = looker_sdk.all_folders()
    return [folder for folder in all_folders if folder.id not in EXCLUDE_FOLDERS]


EXCLUDE_FOLDERS = ['217', '370', '487', '222']


def main():
    sdk = looker_sdk.init40() 
    all_folders = get_all_looker_folders(sdk)
    print(all_folders)
    for folder in all_folders:
        print(f"Checking folder: {folder.name} (ID: {folder.id})")
        # Get Dashboards within the folder
        dashboards = sdk.search_dashboards(folder_id=folder.id)
        for dashboard in dashboards:
            dashboard_id = dashboard.id
            dashboard_name = dashboard.title
            print(f"Dashboard: {dashboard_name} (ID: {dashboard_id})")
            tile_queries = get_dashboard_tile_queries(sdk, dashboard_id)
            for i, query in enumerate(tile_queries, start=1):
                print(f"Tile {i} Query: {query.model}.{query.view}")

if __name__ == '__main__':
    main()