from django.contrib import admin
from . models import (Collection,
                      Product,
                      Supplier,
                      Fabric,
                      Second_layer,
                      Lace,
                      Accessories,
                      Glitter,
                      )


admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Fabric)
admin.site.register(Second_layer)
admin.site.register(Lace)
admin.site.register(Accessories)
admin.site.register(Glitter)