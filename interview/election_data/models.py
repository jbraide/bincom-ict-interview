from django.db import models

class AgentName(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

    class Meta:
        db_table = 'agentname'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class AnnouncedLgaResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_lga_results'

    def __str__(self):
        return f"{self.lga_name} - {self.party_abbreviation} - {self.party_score}"

class AnnouncedPuResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_pu_results'

    def __str__(self):
        return f"Result ID: {self.result_id}"

class AnnouncedStateResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_state_results'

    def __str__(self):
        return f"Result ID: {self.result_id}"

class AnnouncedWardResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'announced_ward_results'

    def __str__(self):
        return f"Result ID: {self.result_id}"

class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'lga'

    def __str__(self):
        return f"LGA: {self.lga_name}"

class Party(models.Model):
    id = models.AutoField(primary_key=True)
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)
    
    class Meta:
        db_table = 'party'

    def __str__(self):
        return f"Party: {self.partyname}"


class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(null=True)
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.TextField(null=True)
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    entered_by_user = models.CharField(max_length=50, null=True)
    date_entered = models.DateTimeField(null=True)
    user_ip_address = models.CharField(max_length=50, null=True)
    
    class Meta:
        db_table = 'polling_unit'

    def __str__(self):
        return f"Polling Unit: {self.polling_unit_name}"

class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'state'

    def __str__(self):
        return f"State: {self.state_name}"

class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'ward'

    def __str__(self):
        return f"Ward: {self.ward_name}"
