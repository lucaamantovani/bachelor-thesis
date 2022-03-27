class AbstractService(StandardPageMetaModel):
    parent = models.ForeignKey(
        ...
    )
    content = JSONField(default=list, blank=True)
    def has_children(self):
        return self.children.filter(is_ready=True)
    class Meta:
       ...