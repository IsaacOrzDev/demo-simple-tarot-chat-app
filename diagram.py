
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.generic.device import Mobile
from diagrams.aws.database import Aurora
from diagrams.aws.blockchain import BlockchainResource
from diagrams.aws.compute import EC2Instance
from diagrams.programming.language import Python
from diagrams.aws.management import SystemsManagerDocuments

with Diagram("", show=False, direction="LR"):
  
  with Cluster(""):
      users = Mobile("Users")
      with Cluster("GCP Cloud Run"):
        application = Python("Application")
        with Cluster("LangChain"):
                summary_llm_chain = BlockchainResource("Conversations Chain")
                retrieval = BlockchainResource("Question Retrieval")
                vector_db = Aurora("Chroma DB")
                documents = SystemsManagerDocuments("Documents related to tarot")
                answer_llm_chain = BlockchainResource("Answer Chain")
      with Cluster("LLMs"):
          cohere = EC2Instance("Cohere")
          open_ai = EC2Instance("OpenAI")

  users >> Edge(label="Ask questions or draw tarot card") >> application

  application >> Edge(label="Summerize conversations ") >> summary_llm_chain
  application >> Edge(label="Send Prompts") >> cohere  >> application
  
  summary_llm_chain >> Edge(label="Gather information") >> retrieval
  retrieval >> Edge(label="Retrieve tarot information") >> vector_db << Edge(label="Embedded") << documents

  retrieval >> Edge(label="Finalize answer") >> answer_llm_chain

  answer_llm_chain >> application >> Edge(label="Response") >> users



