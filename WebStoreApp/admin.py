from django.contrib import admin
from .models import *
# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    exclude = ('deleted_at', 'updated_at', 'created_at', 'created_by_user_id', 'updated_by_user_id', 'deleted_by_user_id', )
    pass
class UserAdmin(BaseAdmin):
    pass

class GenderAdmin(BaseAdmin):
    pass

class PersonAdmin(BaseAdmin):
    pass

class ProductUnitAdmin(BaseAdmin):
    pass

class BranchAdmin(BaseAdmin):
    pass

class ProductImageAdmin(BaseAdmin):
    pass


class ProductCategoryAdmin(BaseAdmin):
    pass

class ProductDepartmentAdmin(BaseAdmin):
    pass

class ProductPricesAdmin(BaseAdmin):
    pass

class ProductBrandAdmin(BaseAdmin):
    pass

class ProductPriceAdmin(BaseAdmin):
    pass

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    exclude = ('deleted_at', 'updated_at', 'created_at', 'created_by_user_id', 'updated_by_user_id', 'deleted_by_user_id', )

class ProductAdmin(BaseAdmin):
    inlines = [ProductImageInline]

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPrice, ProductPriceAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductDepartment, ProductDepartmentAdmin)
admin.site.register(ProductPackage)
admin.site.register(ProductUnit, ProductUnitAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Branch, BranchAdmin)