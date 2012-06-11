task :deploy => [:compass] do
  sh "python deploy.py user.config"
end

task :compass do
  sh("compass compile")  
end
