FROM odoo:16.0
LABEL maintainer="sohaibalabad@gmail.com"
USER root
# Python libraries
# pip3 install pyopenssl==22.0.0     

COPY build_tools/odoo.conf /etc/odoo/odoo.conf
RUN chown odoo /etc/odoo/odoo.conf

COPY ./addons /mnt/addons
COPY ./addons_dependencies /mnt/addons_dependencies
COPY ./addons_extra /mnt/addons_extra

#USER odoo
# TODO JIRA ODOPS-3

HEALTHCHECK CMD curl --fail http://localhost:8069/web/health || exit 1
ENTRYPOINT ["/entrypoint.sh"]

CMD ["odoo"]

