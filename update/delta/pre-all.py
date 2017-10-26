from pum.core.deltapy import DeltaPy
import os

class DropViews(DeltaPy):

    def run(self):

        version = self.current_db_version
        if version > '1.2.8':
            self.drop_views()

    def drop_views(self):
        drop_sql = "{}../../ordinary_data/views/drop_views.sql".format(self.delta_dir)
        pg = self.pg_service

        self.write_message("Dropping views")

        # Compose command
        cmd = 'psql "service = {pg}" -f {drop_sql}'.format(pg=pg, drop_sql=drop_sql)
        self.write_message(cmd)

        # Execute command
        os.system(cmd)
        self.write_message("Dropping views: done")
